import React, { useState, useEffect } from 'react';
import axiosInstance from '../../axios';
import { useHistory, useParams } from 'react-router-dom';
import Button from '@material-ui/core/Button';
import CssBaseline from '@material-ui/core/CssBaseline';
import TextField from '@material-ui/core/TextField';
import Grid from '@material-ui/core/Grid';
import Typography from '@material-ui/core/Typography';
import { makeStyles } from '@material-ui/core/styles';
import Container from '@material-ui/core/Container';

const useStyles = makeStyles((theme) => ({
    paper: {
        marginTop: theme.spacing(8),
        display: 'flex',
        flexDirection: 'column',
        alignItems: 'center',
    },
    form: {
        width: '100%',
        marginTop: theme.spacing(3),
    },
    submit: {
        margin: theme.spacing(3, 0, 2),
    },
}));

export default function Create() {
    const history = useHistory();
    const { id } = useParams();
    const initialFormData = Object.freeze({
        email: '',
        user_name: '',
        account_address: '',
        account_money: '',
        receive_account: '',
        amount: '',
    });

    const [formData, updateFormData] = useState(initialFormData);

    useEffect(() => {
        axiosInstance.get('/user/' + id + '/').then((res) => {
            updateFormData({
                ...formData,
                ['email']: res.data.email,
                ['user_name']: res.data.user_name,
                ['account_address']: res.data.account_address,
                ['account_money']: res.data.account_money,
            });
            console.log(res.data);
        });
    }, [updateFormData]);

    const handleChange = (e) => {
        if ([e.target.name] == 'balance') {
            updateFormData({
                ...formData,
                amount: e.target.value.trim(),
            });
        }
        if ([e.target.name] == 'receive_account') {
            updateFormData({
                ...formData,
                receive_account: e.target.value.trim(),
            });
        }

    };

    const handleSubmit = (e) => {
        e.preventDefault();
        console.log(formData);

        axiosInstance.post(`/transaction/transfer/`, {
            send_account: formData.account_address,
            receive_account: formData.receive_account,
            amount: formData.amount,//6
        });
        history.push({
            pathname: '/admin/',
        });
        window.location.reload();
    };

    const classes = useStyles();

    return (
        <Container component="main" maxWidth="sm">
            <CssBaseline />
            <div className={classes.paper}>
                <Typography component="h1" variant="h5">
                    송금
                </Typography>
                <form className={classes.form} noValidate>
                    <Grid container spacing={2}>
                        <Grid item xs={12}>
                            <TextField
                                disabled="true"
                                variant="outlined"
                                required
                                fullWidth
                                id="user"
                                label="보내는 사람"
                                name="user"
                                autoComplete="user"
                                value={formData.user_name}
                                onChange={handleChange}
                            />
                        </Grid>
                        <Grid item xs={12}>
                            <TextField
                                type="number"
                                disabled="true"
                                variant="outlined"
                                required
                                fullWidth
                                id="account_money"
                                label="계좌 잔액"
                                name="account_money"
                                autoComplete="account_money"
                                value={formData.account_money}
                                onChange={handleChange}
                            />
                        </Grid>
                        <Grid item xs={12}>
                            <TextField
                                type="number"
                                variant="outlined"
                                required
                                fullWidth
                                id="balance"
                                label="금액"
                                name="balance"
                                autoComplete="balance"
                                onChange={handleChange}
                            />
                        </Grid>
                        <Grid item xs={12}>
                            <TextField
                                type="number"
                                disabled="true"
                                variant="outlined"
                                required
                                fullWidth
                                id="send_account"
                                label="출발 주소"
                                name="send_account"
                                autoComplete="send_account"
                                value={formData.account_address}
                                onChange={handleChange}
                            />
                        </Grid>
                        <Grid item xs={12}>
                            <TextField
                                type="number"
                                variant="outlined"
                                required
                                fullWidth
                                id="receive_account"
                                label="목적지 주소"
                                name="receive_account"
                                autoComplete="receive_account"
                                onChange={handleChange}
                                rows={1}
                            />
                        </Grid>
                    </Grid>
                    <Button
                        type="submit"
                        fullWidth
                        variant="contained"
                        color="primary"
                        className={classes.submit}
                        onClick={handleSubmit}
                    >
                        송금
                    </Button>
                </form>
            </div>
        </Container>
    );
}
